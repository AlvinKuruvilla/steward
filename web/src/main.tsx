import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router";

import { TooltipProvider } from "@/components/ui/tooltip";

import App from "@/App";
import "@/index.css";

const router = createBrowserRouter([
  {
    path: "/",
    Component: App,
    children: [
      { index: true, lazy: () => import("@/routes/inbox") },
      { path: ":owner/:name", lazy: () => import("@/routes/inbox") },
      {
        path: ":owner/:name/pulls/:number",
        lazy: () => import("@/routes/pull-request"),
      },
    ],
  },
]);

// Light, until there is a control to change it. Both of OpenWork's surfaces
// are light, the Primer state colours here are their light values, and a dark
// slate ground puts three greys within a few percent of each other.
document.documentElement.dataset.theme = "light";
document.documentElement.style.colorScheme = "light";

const root = document.getElementById("root");
if (!root) throw new Error("index.html has no #root");

createRoot(root).render(
  <StrictMode>
    <QueryClientProvider client={new QueryClient()}>
      <TooltipProvider>
        <RouterProvider router={router} />
      </TooltipProvider>
    </QueryClientProvider>
  </StrictMode>,
);
