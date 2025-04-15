package com.example.goods_sys.controller;

import com.example.goods_sys.entity.BrowseHistory;
import com.example.goods_sys.service.BrowseHistoryService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/browse")
@CrossOrigin(origins = "http://localhost:3001", allowCredentials = "true")
@Slf4j
public class BrowseHistoryController {
    @Autowired
    private BrowseHistoryService browseHistoryService;

    @PostMapping("/add")
    public ResponseEntity<?> addBrowseHistory(@RequestBody BrowseHistory history) {
        try {
            browseHistoryService.addBrowseHistory(history);
            return ResponseEntity.ok().build();
        } catch (Exception e) {
            log.error("添加浏览历史失败", e);
            return ResponseEntity.status(500).body(e.getMessage());
        }
    }

    @GetMapping("/list")
    public ResponseEntity<?> getBrowseHistory() {
        try {
            return ResponseEntity.ok(browseHistoryService.getBrowseHistory());
        } catch (Exception e) {
            log.error("获取浏览历史失败", e);
            return ResponseEntity.status(500).body(e.getMessage());
        }
    }

    @DeleteMapping("/delete")
    public ResponseEntity<?> deleteHistory(@RequestParam String goodUrl) {
        try {
            browseHistoryService.deleteHistory(goodUrl);
            return ResponseEntity.ok().build();
        } catch (Exception e) {
            log.error("删除浏览记录失败", e);
            return ResponseEntity.status(500).body(e.getMessage());
        }
    }

    @DeleteMapping("/clear")
    public ResponseEntity<?> clearAllHistory() {
        try {
            browseHistoryService.clearAllHistory();
            return ResponseEntity.ok().build();
        } catch (Exception e) {
            log.error("清除浏览历史失败", e);
            return ResponseEntity.status(500).body(e.getMessage());
        }
    }
}