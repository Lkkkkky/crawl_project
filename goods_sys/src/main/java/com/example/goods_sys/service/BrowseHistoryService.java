package com.example.goods_sys.service;

import com.example.goods_sys.entity.BrowseHistory;
import com.example.goods_sys.mapper.BrowseHistoryMapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@Slf4j
public class BrowseHistoryService {
    @Autowired
    private BrowseHistoryMapper browseHistoryMapper;

    public void addBrowseHistory(BrowseHistory history) {
        try {
            browseHistoryMapper.addBrowseHistory(history);
        } catch (Exception e) {
            log.error("添加浏览历史失败", e);
            throw new RuntimeException("添加浏览历史失败: " + e.getMessage());
        }
    }

    public List<BrowseHistory> getBrowseHistory() {
        try {
            return browseHistoryMapper.getBrowseHistory();
        } catch (Exception e) {
            log.error("获取浏览历史失败", e);
            throw new RuntimeException("获取浏览历史失败: " + e.getMessage());
        }
    }

    public void deleteHistory(String goodUrl) {
        try {
            browseHistoryMapper.deleteHistory(goodUrl);
        } catch (Exception e) {
            log.error("删除浏览记录失败", e);
            throw new RuntimeException("删除浏览记录失败: " + e.getMessage());
        }
    }

    public void clearAllHistory() {
        try {
            browseHistoryMapper.clearAllHistory();
        } catch (Exception e) {
            log.error("清除浏览历史失败", e);
            throw new RuntimeException("清除浏览历史失败: " + e.getMessage());
        }
    }
}