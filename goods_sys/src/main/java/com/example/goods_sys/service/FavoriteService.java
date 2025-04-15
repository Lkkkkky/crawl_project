package com.example.goods_sys.service;

import com.example.goods_sys.entity.Favorite;
import com.example.goods_sys.mapper.FavoriteMapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@Slf4j
public class FavoriteService {
    @Autowired
    private FavoriteMapper favoriteMapper;

    public void addFavorite(Favorite favorite) {
        try {
            favoriteMapper.addFavorite(favorite);
        } catch (Exception e) {
            log.error("添加收藏失败", e);
            throw new RuntimeException("添加收藏失败: " + e.getMessage());
        }
    }

    public void removeFavorite(String goodUrl) {
        try {
            favoriteMapper.removeFavorite(goodUrl);
        } catch (Exception e) {
            log.error("取消收藏失败", e);
            throw new RuntimeException("取消收藏失败: " + e.getMessage());
        }
    }

    public List<String> checkFavorites(List<String> goodUrls) {
        try {
            return favoriteMapper.checkFavorites(goodUrls);
        } catch (Exception e) {
            log.error("检查收藏状态失败", e);
            throw new RuntimeException("检查收藏状态失败: " + e.getMessage());
        }
    }

    public List<Favorite> getFavorites() {
        try {
            return favoriteMapper.getFavorites();
        } catch (Exception e) {
            log.error("获取收藏列表失败", e);
            throw new RuntimeException("获取收藏列表失败: " + e.getMessage());
        }
    }
}