package com.example.goods_sys.mapper;

import com.example.goods_sys.entity.Favorite;
import org.apache.ibatis.annotations.*;
import java.util.List;

@Mapper
public interface FavoriteMapper {
        @Insert("INSERT INTO favorites (good_url, good_name, good_price, good_source, favorite_time) " +
                        "VALUES (#{good_url}, #{good_name}, #{good_price}, #{good_source}, NOW())")
        void addFavorite(Favorite favorite);

        @Delete("DELETE FROM favorites WHERE good_url = #{goodUrl}")
        void removeFavorite(String goodUrl);

        @Select("SELECT good_url FROM favorites WHERE good_url IN " +
                        "<foreach item='url' collection='goodUrls' open='(' separator=',' close=')'>" +
                        "#{url}" +
                        "</foreach>")
        List<String> checkFavorites(@Param("goodUrls") List<String> goodUrls);

        @Select("SELECT * FROM favorites ORDER BY favorite_time DESC")
        List<Favorite> getFavorites();

        @Delete("DELETE FROM favorites")
        void clearAllFavorites();
}