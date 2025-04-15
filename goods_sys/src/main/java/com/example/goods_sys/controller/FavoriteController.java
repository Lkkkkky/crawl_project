package com.example.goods_sys.controller;

import com.example.goods_sys.entity.Favorite;
import com.example.goods_sys.service.FavoriteService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/favorites")
@CrossOrigin(origins = "http://localhost:3001", allowCredentials = "true")
@Slf4j
public class FavoriteController {
    @Autowired
    private FavoriteService favoriteService;

    @PostMapping("/add")
    public ResponseEntity<?> addFavorite(@RequestBody Favorite favorite) {
        try {
            favoriteService.addFavorite(favorite);
            return ResponseEntity.ok().build();
        } catch (Exception e) {
            log.error("添加收藏失败", e);
            return ResponseEntity.status(500).body(e.getMessage());
        }
    }

    @DeleteMapping("/remove")
    public ResponseEntity<?> removeFavorite(@RequestParam String goodUrl) {
        try {
            favoriteService.removeFavorite(goodUrl);
            return ResponseEntity.ok().build();
        } catch (Exception e) {
            log.error("取消收藏失败", e);
            return ResponseEntity.status(500).body(e.getMessage());
        }
    }

    @GetMapping("/check")
    public ResponseEntity<?> checkFavorites(@RequestParam List<String> goodUrls) {
        try {
            return ResponseEntity.ok(favoriteService.checkFavorites(goodUrls));
        } catch (Exception e) {
            log.error("检查收藏状态失败", e);
            return ResponseEntity.status(500).body(e.getMessage());
        }
    }

    @GetMapping("/list")
    public ResponseEntity<?> getFavorites() {
        try {
            return ResponseEntity.ok(favoriteService.getFavorites());
        } catch (Exception e) {
            log.error("获取收藏列表失败", e);
            return ResponseEntity.status(500).body(e.getMessage());
        }
    }
}