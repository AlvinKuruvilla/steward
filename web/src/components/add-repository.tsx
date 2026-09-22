import { useMutation, useQueryClient } from "@tanstack/react-query";
import { useState } from "react";

import { post, type Repository } from "@/api";

/** Adding a repository is the app's job, not the terminal's. */
export function AddRepository() {
  const [value, setValue] = useState("");
  const client = useQueryClient();

  const add = useMutation({
    mutationFn: (repository: string) => {
      const [owner, name] = repository.split("/");
      if (!owner || !name) throw new Error("expected owner/repo");
      return post<Repository>("/api/repositories", { owner, name });
    },
    onSuccess: () => {
      setValue("");
      void client.invalidateQueries({ queryKey: ["repositories"] });
    },
  });

  return (
    <form
      className="flex items-center gap-2"
      onSubmit={(event) => {
        event.preventDefault();
        add.mutate(value.trim());
      }}
    >
      <input
        className="derived w-56 rounded-[var(--radius-row)] border border-[var(--color-line)] bg-[var(--color-app)] px-2 py-1 outline-none focus:border-[var(--color-secondary)]"
        placeholder="owner/repo"
        value={value}
        onChange={(event) => setValue(event.target.value)}
        aria-label="repository to sync"
      />
      <button
        type="submit"
        disabled={value.trim() === "" || add.isPending}
        className="rounded-[var(--radius-row)] bg-[var(--color-accent)] px-3 py-1 text-sm text-white disabled:opacity-40"
      >
        {add.isPending ? "Starting…" : "Sync"}
      </button>
      {add.error ? (
        <span className="text-xs text-[var(--color-state-closed)]">
          {add.error.message}
        </span>
      ) : null}
    </form>
  );
}
