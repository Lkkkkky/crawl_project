package com.example.goods_sys.mapper;

import com.example.goods_sys.entity.BrowseHistory;
import org.apache.ibatis.annotations.*;
import java.util.List;
import java.util.Date;

@Mapper
public interface BrowseHistoryMapper {
    @Insert("INSERT INTO browse_history (good_url, good_name, good_price, good_source, browse_time) " +
            "VALUES (#{good_url}, #{good_name}, #{good_price}, #{good_source}, NOW())")
    void addBrowseHistory(BrowseHistory history);

    @Select("SELECT * FROM browse_history ORDER BY browse_time DESC")
    @Results({
            @Result(property = "good_url", column = "good_url"),
            @Result(property = "good_name", column = "good_name"),
            @Result(property = "good_price", column = "good_price"),
            @Result(property = "good_source", column = "good_source"),
            @Result(property = "browse_time", column = "browse_time")
    })
    List<BrowseHistory> getBrowseHistory();

    @Delete("DELETE FROM browse_history WHERE good_url = #{goodUrl}")
    void deleteHistory(@Param("goodUrl") String goodUrl);

    @Delete("DELETE FROM browse_history")
    void clearAllHistory();
}