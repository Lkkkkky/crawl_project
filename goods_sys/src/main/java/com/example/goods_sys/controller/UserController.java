package com.example.goods_sys.controller;

import com.example.goods_sys.entity.User;
import com.example.goods_sys.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api/user")
@CrossOrigin(origins = "http://localhost:3001", allowCredentials = "true")
public class UserController {
    @Autowired
    private UserService userService;

    @PostMapping("/register")
    public Map<String, Object> register(@RequestBody User user) {
        Map<String, Object> result = new HashMap<>();
        boolean success = userService.register(user);
        result.put("success", success);
        result.put("message", success ? "注册成功" : "用户名已存在");
        return result;
    }

    @PostMapping("/login")
    public Map<String, Object> login(@RequestBody User user) {
        Map<String, Object> result = new HashMap<>();
        User loginUser = userService.login(user);
        if (loginUser != null) {
            result.put("success", true);
            result.put("message", "登录成功");
            result.put("token", "user-token-" + loginUser.getUsername()); // 简单token生成
            result.put("user", loginUser);
        } else {
            result.put("success", false);
            result.put("message", "用户名或密码错误");
        }
        return result;
    }
}