import { useMutation, useQueryClient } from "@tanstack/react-query";
import { useState } from "react";

import { post, type Repository } from "@/api";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

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
      {add.error ? (
        <span className="text-xs text-destructive">{add.error.message}</span>
      ) : null}
      <Input
        className="font-mono h-8 w-52 text-xs"
        placeholder="owner/repo"
        value={value}
        onChange={(event) => setValue(event.target.value)}
        aria-label="repository to read"
      />
      <Button
        type="submit"
        variant="outline"
        size="sm"
        disabled={value.trim() === "" || add.isPending}
      >
        {add.isPending ? "Reading" : "Read"}
      </Button>
    </form>
  );
}
