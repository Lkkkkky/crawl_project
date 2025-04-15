import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Login.css";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    if (username === "admin" && password === "password") {
      alert("登录成功！");
      navigate("/home");
      localStorage.setItem("isLoggedIn", true); // 模拟登录状态

    } else {
      alert("用户名或密码错误！");
    }
  };

  return (
    <div className="login-container">
      <h1>登录</h1>
      <form onSubmit={handleLogin}>
        <input
          type="text"
          placeholder="用户名"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="密码"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">登录</button>
      </form>
      <p>
        没有账号？ <a href="/register">去注册</a>
      </p>
    </div>
  );
}

export default Login;
