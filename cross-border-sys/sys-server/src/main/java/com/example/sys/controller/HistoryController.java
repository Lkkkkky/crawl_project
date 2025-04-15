package com.example.sys.controller;

import com.example.sys.dto.ApiResponse;
import com.example.sys.entity.History;
import com.example.sys.entity.User;
import com.example.sys.service.HistoryService;
import com.example.sys.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.web.bind.annotation.*;

import java.security.Principal;

@RestController
@RequestMapping("/api/history")
@RequiredArgsConstructor
public class HistoryController {
    private final HistoryService historyService;
    private final UserService userService;

    @GetMapping
    public ApiResponse<Page<History>> getUserHistory(Principal principal,
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size) {
        User user = userService.findByUsername(principal.getName());
        return ApiResponse.success(
            historyService.getUserHistory(user, PageRequest.of(page, size))
        );
    }

    @DeleteMapping("/{id}")
    public ApiResponse<?> deleteHistory(@PathVariable Long id) {
        // TODO: 从Session获取当前用户
        User user = userService.findByUsername("testuser");
        historyService.deleteHistory(id, user);
        return ApiResponse.success(null);
    }
} 