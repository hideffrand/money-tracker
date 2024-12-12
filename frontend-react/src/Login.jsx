import { useRef } from "react";
import { useNavigate } from "react-router-dom";
import { API_BASE_URL } from "./config";

export default function Login() {
  const navigate = useNavigate();
  const emailRef = useRef();
  const passwordRef = useRef();

  async function handleLogin(e) {
    e.preventDefault();
    if (!emailRef.current.value || !passwordRef.current.value) {
      return alert("Please fill in both fields");
    }

    const res = await fetch(`${API_BASE_URL}/auth/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: emailRef.current.value,
        password: passwordRef.current.value,
      }),
    });

    if (!res.ok) return alert("Failed to Login");
    const parsed = await res.json();

    const token = parsed.data.token;
    document.cookie = `token=${token}; path=/; max-age=3600`;

    const userId = parsed.data.user.user_id;
    document.cookie = `userId=${userId}; path=/; max-age=3600`;

    alert("Login Success!");
    return navigate("/");
  }

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <div className="bg-white p-8 rounded-lg shadow-lg w-full max-w-sm">
        <h2 className="text-2xl font-bold text-center text-gray-700 mb-6">
          Login
        </h2>
        <form className="space-y-4" onSubmit={handleLogin}>
          <input
            ref={emailRef}
            type="email"
            placeholder="Email"
            className="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
          />
          <input
            ref={passwordRef}
            type="password"
            placeholder="Password"
            className="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
          />
          <button
            type="submit"
            className="w-full py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition duration-200"
            // onClick={handleLogin}
          >
            Login
          </button>
        </form>
      </div>
    </div>
  );
}
