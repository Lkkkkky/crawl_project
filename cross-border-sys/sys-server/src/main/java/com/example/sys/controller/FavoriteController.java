package com.example.sys.controller;

import com.example.sys.dto.ApiResponse;
import com.example.sys.entity.Favorite;
import com.example.sys.entity.Product;
import com.example.sys.entity.User;
import com.example.sys.service.FavoriteService;
import com.example.sys.service.ProductService;
import com.example.sys.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/favorites")
@RequiredArgsConstructor
public class FavoriteController {
    private final FavoriteService favoriteService;
    private final UserService userService;
    private final ProductService productService;

    @GetMapping
    public ApiResponse<Page<Favorite>> getUserFavorites(
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size) {
        // TODO: 从Session获取当前用户
        User user = userService.findByUsername("testuser");
        return ApiResponse.success(
            favoriteService.getUserFavorites(user, PageRequest.of(page, size))
        );
    }

    @PostMapping
    public ApiResponse<?> addFavorite(@RequestParam String productId) {
        // TODO: 从Session获取当前用户
        User user = userService.findByUsername("testuser");
        Product product = productService.getProduct(productId);
        favoriteService.addFavorite(user, product);
        return ApiResponse.success(null);
    }

    @DeleteMapping("/{id}")
    public ApiResponse<?> deleteFavorite(@PathVariable Long id) {
        // TODO: 从Session获取当前用户
        User user = userService.findByUsername("testuser");
        favoriteService.deleteFavorite(id, user);
        return ApiResponse.success(null);
    }
} 