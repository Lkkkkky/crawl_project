package com.example.goods_sys.controller;

import com.example.goods_sys.entity.Goods;
import com.example.goods_sys.service.GoodsService;
import com.github.pagehelper.PageInfo;
import lombok.Data;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/goods")
@CrossOrigin(origins = "http://localhost:3001", allowCredentials = "true")
@Slf4j
public class GoodsController {
    @Autowired
    private GoodsService goodsService;

    @GetMapping("/test")
    public String test() {
        return "API is working!";
    }

    @GetMapping("/search")
    public ResponseEntity<?> searchGoods(
            @RequestParam String keyword,
            @RequestParam(defaultValue = "1") int pageNum,
            @RequestParam(defaultValue = "10") int pageSize,
            @RequestParam(required = false) String platform) {
        try {
            log.debug("接收到搜索请求: keyword={}, pageNum={}, pageSize={}, platform={}",
                    keyword, pageNum, pageSize, platform);
            PageInfo<Goods> result = goodsService.searchGoods(keyword, pageNum, pageSize, platform);
            log.debug("搜索完成，返回结果数量: {}", result.getList().size());
            return ResponseEntity.ok(result);
        } catch (Exception e) {
            log.error("搜索商品失败", e);
            return ResponseEntity.status(500)
                    .body(new ErrorResponse("搜索商品失败: " + e.getMessage()));
        }
    }
}

@Data
class ErrorResponse {
    private String message;

    public ErrorResponse(String message) {
        this.message = message;
    }
}