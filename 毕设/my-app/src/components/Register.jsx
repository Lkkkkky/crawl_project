import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Register.css";

function Register() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const navigate = useNavigate();

  const handleRegister = (e) => {
    e.preventDefault();
    // 简单验证逻辑
    if (password !== confirmPassword) {
      alert("两次输入的密码不一致！");
      return;
    }
    alert("注册成功！");
    navigate("/login"); // 跳转到登录页面
  };

  return (
    <div className="register-container">
      <h1>注册</h1>
      <form onSubmit={handleRegister}>
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
        <input
          type="password"
          placeholder="确认密码"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
        />
        <button type="submit">注册</button>
      </form>
      <p>
        已有账号？ <a href="/login">去登录</a>
      </p>
    </div>
  );
}

export default Register;
