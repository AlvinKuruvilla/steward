/**
 * The keyboard map, on demand.
 *
 * `?` is the binding GitHub, Gmail and Linear all use for this, so the panel
 * needs no permanent legend in the header -- the affordance is one icon, and
 * the bindings themselves cost nothing until asked for.
 */
import { Keyboard } from "lucide-react";
import { useEffect, useState } from "react";

import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { typing } from "@/keys";

const bindings: [string[], string][] = [
  [["j", "k"], "Move down and up the queue"],
  [["↵"], "Open the pull request"],
  [["o"], "Open it on GitHub"],
  [["?"], "Show this"],
];

export function Shortcuts() {
  const [open, setOpen] = useState(false);

  useEffect(() => {
    function onKey(event: KeyboardEvent) {
      if (event.key !== "?" || typing(event.target)) return;
      event.preventDefault();
      setOpen((was) => !was);
    }
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, []);

  return (
    <>
      <Button
        size="icon-sm"
        variant="ghost"
        aria-label="Keyboard shortcuts"
        title="Keyboard shortcuts (?)"
        className="text-muted-foreground"
        onClick={() => setOpen(true)}
      >
        <Keyboard className="size-4" aria-hidden />
      </Button>

      <Dialog open={open} onOpenChange={setOpen}>
        <DialogContent className="sm:max-w-sm">
          <DialogHeader>
            <DialogTitle>Keyboard</DialogTitle>
            <DialogDescription>
              The queue is meant to be walked without the mouse.
            </DialogDescription>
          </DialogHeader>
          <dl className="flex flex-col gap-2.5">
            {bindings.map(([keys, means]) => (
              <div key={means} className="flex items-baseline gap-3">
                <dt className="flex w-16 shrink-0 gap-1">
                  {keys.map((key) => (
                    <kbd
                      key={key}
                      className="min-w-5 rounded border border-border bg-muted px-1 text-center font-mono text-[11px] leading-5 text-foreground"
                    >
                      {key}
                    </kbd>
                  ))}
                </dt>
                <dd className="text-[13px] text-muted-foreground">{means}</dd>
              </div>
            ))}
          </dl>
        </DialogContent>
      </Dialog>
    </>
  );
}
