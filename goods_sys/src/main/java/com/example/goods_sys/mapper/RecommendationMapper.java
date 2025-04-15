package com.example.goods_sys.mapper;

import com.example.goods_sys.entity.Recommendation;
import org.apache.ibatis.annotations.*;
import java.util.List;

@Mapper
public interface RecommendationMapper {
        @Insert("INSERT INTO recommendations (username, good_url, good_name, good_source, similarity_score, recommend_time) "
                        +
                        "VALUES (#{username}, #{good_url}, #{good_name}, #{good_source}, #{similarity_score}, NOW())")
        void addRecommendation(Recommendation recommendation);

        @Select("SELECT * FROM recommendations WHERE username = #{username} ORDER BY similarity_score DESC, recommend_time DESC")
        @Results({
                        @Result(property = "username", column = "username"),
                        @Result(property = "good_url", column = "good_url"),
                        @Result(property = "good_name", column = "good_name"),

                        @Result(property = "good_source", column = "good_source"),
                        @Result(property = "similarity_score", column = "similarity_score"),
                        @Result(property = "recommend_time", column = "recommend_time")
        })
        List<Recommendation> getRecommendations(@Param("username") String username);

        @Delete("DELETE FROM recommendations WHERE username = #{username}")
        void clearUserRecommendations(@Param("username") String username);

        @Delete("DELETE FROM recommendations WHERE username = #{username} AND good_url = #{goodUrl}")
        void removeRecommendation(@Param("username") String username, @Param("goodUrl") String goodUrl);

        @Select("SELECT DISTINCT r.* FROM recommendations r " +
                        "INNER JOIN browse_history b ON r.good_source = b.good_source " +
                        "WHERE r.username = #{username} AND b.good_url = #{goodUrl} " +
                        "ORDER BY r.similarity_score DESC LIMIT 5")
        List<Recommendation> getSimilarItems(@Param("username") String username, @Param("goodUrl") String goodUrl);
}