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
        className="derived h-7 w-52 rounded-[var(--radius-row)] border border-[var(--color-line)] bg-[var(--color-app)] px-2 text-[12px] text-[var(--color-ink)] placeholder:text-[var(--color-muted)] focus:border-[var(--slate-8)] focus:outline-none"
        placeholder="owner/repo"
        value={value}
        onChange={(event) => setValue(event.target.value)}
        aria-label="repository to sync"
      />
      <button
        type="submit"
        disabled={value.trim() === "" || add.isPending}
        className="h-7 rounded-[var(--radius-row)] px-2.5 text-[12px] text-[var(--color-muted)] transition-colors duration-100 hover:bg-[var(--color-hover)] hover:text-[var(--color-ink)] disabled:pointer-events-none disabled:opacity-40"
      >
        {add.isPending ? "Starting" : "Sync"}
      </button>
      {add.error ? (
        <span className="text-[12px] text-[var(--color-closed)]">
          {add.error.message}
        </span>
      ) : null}
    </form>
  );
}
