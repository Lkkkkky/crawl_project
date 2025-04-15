package com.example.goods_sys.mapper;

import com.example.goods_sys.entity.Goods;
import org.apache.ibatis.annotations.*;
import java.util.List;

@Mapper
public interface GoodsMapper {
    @Select("SELECT good_name, good_price, good_url, good_source FROM goods_list FORCE INDEX(idx_good_name) " +
            "WHERE good_name LIKE CONCAT('%', REPLACE(REPLACE(#{keyword}, '_', '\\_'), '%', '\\%'), '%') " +
            "AND (#{platform} IS NULL OR #{platform} = '' OR good_source = #{platform})")
    @Results({
            @Result(property = "good_name", column = "good_name"),
            @Result(property = "good_price", column = "good_price"),
            @Result(property = "good_url", column = "good_url"),
            @Result(property = "good_source", column = "good_source")
    })
    List<Goods> searchGoods(@Param("keyword") String keyword, @Param("platform") String platform);
}