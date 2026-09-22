/**
 * Light or dark, chosen by the person and remembered.
 *
 * The attribute is what the stylesheet reads; `colorScheme` is what the
 * browser reads for scrollbars and form controls, and they have to agree or
 * the chrome ends up light on a dark page.
 */
import { useSyncExternalStore } from "react";

export type Theme = "light" | "dark";

const KEY = "steward.theme";
const listeners = new Set<() => void>();

function systemTheme(): Theme {
  return window.matchMedia("(prefers-color-scheme: dark)").matches
    ? "dark"
    : "light";
}

export function storedTheme(): Theme {
  const saved = localStorage.getItem(KEY);
  return saved === "light" || saved === "dark" ? saved : systemTheme();
}

export function applyTheme(theme: Theme): void {
  document.documentElement.dataset.theme = theme;
  document.documentElement.style.colorScheme = theme;
}

export function setTheme(theme: Theme): void {
  localStorage.setItem(KEY, theme);
  applyTheme(theme);
  for (const listener of listeners) listener();
}

export function useTheme(): [Theme, (theme: Theme) => void] {
  const theme = useSyncExternalStore(
    (listener) => {
      listeners.add(listener);
      return () => listeners.delete(listener);
    },
    () => (document.documentElement.dataset.theme as Theme) ?? "light",
    () => "light" as Theme,
  );
  return [theme, setTheme];
}
