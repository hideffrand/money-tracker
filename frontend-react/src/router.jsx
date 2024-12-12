import { BrowserRouter, Routes, Route } from "react-router-dom";
import App from "./App";
import Login from "./Login";

export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </BrowserRouter>
  );
}
