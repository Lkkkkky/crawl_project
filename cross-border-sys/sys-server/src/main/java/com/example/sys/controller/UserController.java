package com.example.sys.controller;

import com.example.sys.dto.ApiResponse;
import com.example.sys.dto.RegisterRequest;
import com.example.sys.entity.User;
import com.example.sys.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.security.Principal;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.password.PasswordEncoder;
import com.example.sys.dto.LoginRequest;
import com.example.sys.dto.LoginResponse;

@RestController
@RequestMapping("/api/auth")
@RequiredArgsConstructor
public class UserController {
    private final UserService userService;
    private final AuthenticationManager authenticationManager;

    @PostMapping("/register")
    public ApiResponse<User> register(@Valid @RequestBody RegisterRequest request) {
        try {
            User user = userService.register(request.getUsername(), request.getPassword());
            return ApiResponse.success(user);
        } catch (Exception e) {
            return ApiResponse.error(e.getMessage());
        }
    }

    @PostMapping("/login")
    public ApiResponse<LoginResponse> login(@Valid @RequestBody LoginRequest request) {
        try {
            Authentication authentication = authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(
                    request.getUsername(),
                    request.getPassword()
                )
            );
            
            SecurityContextHolder.getContext().setAuthentication(authentication);
            
            LoginResponse response = new LoginResponse();
            response.setUsername(request.getUsername());
            return ApiResponse.success(response);
        } catch (AuthenticationException e) {
            return ApiResponse.error("Invalid username or password");
        }
    }

    @GetMapping("/current")
    public ApiResponse<User> getCurrentUser(Principal principal) {
        if (principal == null) {
            return ApiResponse.error("Not logged in");
        }
        User user = userService.findByUsername(principal.getName());
        return ApiResponse.success(user);
    }
} 