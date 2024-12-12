import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import Router from "./router";
import ModalProvider from "./contexts/ModalContext";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <ModalProvider>
      <Router />
    </ModalProvider>
  </StrictMode>
);
