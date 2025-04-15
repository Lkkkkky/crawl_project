package com.example.goods_sys.service;

import com.example.goods_sys.entity.BrowseHistory;
import com.example.goods_sys.entity.Favorite;
import com.example.goods_sys.entity.Recommendation;
import com.example.goods_sys.mapper.BrowseHistoryMapper;
import com.example.goods_sys.mapper.FavoriteMapper;
import com.example.goods_sys.mapper.RecommendationMapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.*;
import java.util.stream.Collectors;

@Service
@Slf4j
public class RecommendationService {

    public void removeRecommendation(String username, String goodUrl) {
        try {
            recommendationMapper.removeRecommendation(username, goodUrl);
        } catch (Exception e) {
            log.error("删除推荐商品失败", e);
            throw new RuntimeException("删除推荐商品失败: " + e.getMessage());
        }
    }

    @Autowired
    private RecommendationMapper recommendationMapper;

    @Autowired
    private BrowseHistoryMapper browseHistoryMapper;

    @Autowired
    private FavoriteMapper favoriteMapper;

    public List<Recommendation> getRecommendations(String username) {
        try {
            return recommendationMapper.getRecommendations(username);
        } catch (Exception e) {
            log.error("获取推荐商品失败", e);
            throw new RuntimeException("获取推荐商品失败: " + e.getMessage());
        }
    }

    public void clearRecommendations(String username) {
        try {
            recommendationMapper.clearUserRecommendations(username);
        } catch (Exception e) {
            log.error("清空推荐商品失败", e);
            throw new RuntimeException("清空推荐商品失败: " + e.getMessage());
        }
    }

    public void generateRecommendations(String username) {
        try {
            // 清除用户之前的推荐记录
            clearRecommendations(username);

            // 获取用户的浏览历史和收藏记录
            List<BrowseHistory> browseHistories = browseHistoryMapper.getBrowseHistory();
            List<Favorite> favorites = favoriteMapper.getFavorites();

            // 合并用户行为数据
            Map<String, Double> userPreferences = new HashMap<>();

            // 浏览历史权重为1.0
            browseHistories.forEach(history -> {
                userPreferences.put(history.getGood_source(),
                        userPreferences.getOrDefault(history.getGood_source(), 0.0) + 1.0);
            });

            // 收藏记录权重为2.0
            favorites.forEach(favorite -> {
                userPreferences.put(favorite.getGood_source(),
                        userPreferences.getOrDefault(favorite.getGood_source(), 0.0) + 2.0);
            });

            // 计算商品相似度并生成推荐
            List<Recommendation> recommendations = new ArrayList<>();
            Set<String> sources = userPreferences.keySet();

            for (String source : sources) {
                double userWeight = userPreferences.get(source);

                // 获取相似商品
                List<BrowseHistory> similarItems = browseHistoryMapper.getBrowseHistory().stream()
                        .filter(item -> !item.getGood_source().equals(source))
                        .collect(Collectors.toList());

                // 计算相似度并生成推荐
                for (BrowseHistory item : similarItems) {
                    Recommendation recommendation = new Recommendation();
                    recommendation.setUsername(username);
                    recommendation.setGood_url(item.getGood_url());
                    recommendation.setGood_name(item.getGood_name());

                    recommendation.setGood_source(item.getGood_source());

                    // 计算相似度分数
                    double similarityScore = calculateSimilarityScore(source, item.getGood_source(), userWeight);
                    recommendation.setSimilarity_score(similarityScore);

                    recommendations.add(recommendation);
                }
            }

            // 按相似度排序并保存推荐结果
            recommendations.sort((a, b) -> b.getSimilarity_score().compareTo(a.getSimilarity_score()));
            recommendations.stream()
                    .limit(20) // 限制推荐数量
                    .forEach(recommendation -> recommendationMapper.addRecommendation(recommendation));

        } catch (Exception e) {
            log.error("生成推荐商品失败", e);
            throw new RuntimeException("生成推荐商品失败: " + e.getMessage());
        }
    }

    private double calculateSimilarityScore(String source1, String source2, double userWeight) {
        // 基于商品来源的简单相似度计算
        if (source1.equals(source2)) {
            return 1.0 * userWeight;
        }
        // 不同来源的商品，基于用户权重计算相似度
        return 0.5 * userWeight;
    }

    public List<Recommendation> getSimilarItems(String username, String goodUrl) {
        try {
            return recommendationMapper.getSimilarItems(username, goodUrl);
        } catch (Exception e) {
            log.error("获取相似商品失败", e);
            throw new RuntimeException("获取相似商品失败: " + e.getMessage());
        }
    }
}