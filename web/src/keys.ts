/**
 * Keyboard navigation for the queue.
 *
 * `j`/`k` move, `enter` opens, `o` opens on GitHub -- the bindings GitHub and
 * every mail client already trained maintainers on. `?` is handled by the
 * panel that lists them, mounted in the shell. Typing in a field is left alone,
 * or the repository box would eat every keystroke.
 */
import { useEffect } from "react";

export interface Keymap {
  next: () => void;
  previous: () => void;
  open: () => void;
  openExternally: () => void;
}

export function typing(target: EventTarget | null): boolean {
  if (!(target instanceof HTMLElement)) return false;
  return (
    target.isContentEditable ||
    ["INPUT", "TEXTAREA", "SELECT"].includes(target.tagName)
  );
}

export function useKeys(keymap: Keymap): void {
  useEffect(() => {
    function onKey(event: KeyboardEvent) {
      if (typing(event.target) || event.metaKey || event.ctrlKey) return;

      const act = {
        j: keymap.next,
        ArrowDown: keymap.next,
        k: keymap.previous,
        ArrowUp: keymap.previous,
        Enter: keymap.open,
        o: keymap.openExternally,
      }[event.key];

      if (act) {
        event.preventDefault();
        act();
      }
    }

    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [keymap]);
}
