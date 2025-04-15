package com.example.goods_sys.controller;

import com.example.goods_sys.entity.Recommendation;
import com.example.goods_sys.service.RecommendationService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/recommendations")
@CrossOrigin(origins = "http://localhost:3001", allowCredentials = "true")
@Slf4j
public class RecommendationController {
    @Autowired
    private RecommendationService recommendationService;

    @DeleteMapping("/clear")
    public ResponseEntity<?> clearRecommendations(@RequestParam String username) {
        try {
            recommendationService.clearRecommendations(username);
            return ResponseEntity.ok().build();
        } catch (Exception e) {
            log.error("清空推荐商品失败", e);
            return ResponseEntity.status(500).body(e.getMessage());
        }
    }

    @GetMapping("/list")
    public ResponseEntity<?> getRecommendations(@RequestParam String username) {
        try {
            List<Recommendation> recommendations = recommendationService.getRecommendations(username);
            return ResponseEntity.ok(recommendations);
        } catch (Exception e) {
            log.error("获取推荐商品失败", e);
            return ResponseEntity.status(500).body(e.getMessage());
        }
    }

    @PostMapping("/generate")
    public ResponseEntity<?> generateRecommendations(@RequestParam String username) {
        try {
            recommendationService.generateRecommendations(username);
            return ResponseEntity.ok().build();
        } catch (Exception e) {
            log.error("生成推荐商品失败", e);
            return ResponseEntity.status(500).body(e.getMessage());
        }
    }

    @DeleteMapping("/remove")
    public ResponseEntity<?> removeRecommendation(@RequestParam String username, @RequestParam String goodUrl) {
        try {
            recommendationService.removeRecommendation(username, goodUrl);
            return ResponseEntity.ok().build();
        } catch (Exception e) {
            log.error("删除推荐商品失败", e);
            return ResponseEntity.status(500).body(e.getMessage());
        }
    }

    @GetMapping("/similar")
    public ResponseEntity<?> getSimilarItems(@RequestParam String username, @RequestParam String goodUrl) {
        try {
            List<Recommendation> similarItems = recommendationService.getSimilarItems(username, goodUrl);
            return ResponseEntity.ok(similarItems);
        } catch (Exception e) {
            log.error("获取相似商品失败", e);
            return ResponseEntity.status(500).body(e.getMessage());
        }
    }
}