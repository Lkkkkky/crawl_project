package com.example.goods_sys.service;

import com.example.goods_sys.entity.Goods;
import com.example.goods_sys.mapper.GoodsMapper;
import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.ArrayList;

@Service
@Slf4j
public class GoodsService {
    @Autowired
    private GoodsMapper goodsMapper;

    public PageInfo<Goods> searchGoods(String keyword, int pageNum, int pageSize, String platform) {
        try {
            log.debug("开始搜索商品: keyword={}, pageNum={}, pageSize={}, platform={}",
                    keyword, pageNum, pageSize, platform);
            PageHelper.startPage(pageNum, pageSize);
            List<Goods> list = goodsMapper.searchGoods(keyword, platform);
            log.debug("数据库查询结果: {}", list);
            if (list == null) {
                log.warn("查询结果为null");
                list = new ArrayList<>();
            }
            PageInfo<Goods> pageInfo = new PageInfo<>(list);
            log.debug("分页信息: total={}, pages={}", pageInfo.getTotal(), pageInfo.getPages());
            return pageInfo;
        } catch (Exception e) {
            log.error("搜索商品时发生异常", e);
            throw new RuntimeException("搜索商品失败: " + e.getMessage(), e);
        }
    }
}