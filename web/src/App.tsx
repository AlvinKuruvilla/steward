/**
 * The shell: a repository switcher, a sidebar, and whatever the route renders.
 * Layout follows docs/design/0002-visual-language.md -- 16px outside, tight
 * inside, borders between rows rather than gaps.
 */
import { NavLink, Outlet } from "react-router";

const sections = [
  { to: "/", label: "Inbox" },
  { to: "/pulls", label: "PRs" },
  { to: "/bots", label: "Bots" },
];

export default function App() {
  return (
    <div className="min-h-screen p-4">
      <div className="mx-auto flex max-w-6xl flex-col overflow-hidden rounded-[var(--radius-shell)] border border-[var(--color-line)] bg-[var(--color-panel)] shadow-[var(--shadow-shell)]">
        <header className="flex items-baseline justify-between border-b border-[var(--color-line)] px-4 py-3">
          <span className="derived">precogly/precogly</span>
          <span className="text-xs text-[var(--color-secondary)]">
            not yet synced
          </span>
        </header>

        <div className="flex min-h-[32rem]">
          <nav className="w-40 shrink-0 border-r border-[var(--color-line)] p-2">
            {sections.map((section) => (
              <NavLink
                key={section.to}
                to={section.to}
                className={({ isActive }) =>
                  `block rounded-[var(--radius-row)] px-3 py-2 text-sm ${
                    isActive
                      ? "bg-[var(--color-active)] text-[var(--color-primary)]"
                      : "text-[var(--color-secondary)] hover:bg-[var(--color-hover)]"
                  }`
                }
                end={section.to === "/"}
              >
                {section.label}
              </NavLink>
            ))}
          </nav>

          <main className="flex-1 p-4">
            <Outlet />
          </main>
        </div>
      </div>
    </div>
  );
}
