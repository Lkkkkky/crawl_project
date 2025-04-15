package com.example.goods_sys.mapper;

import com.example.goods_sys.entity.User;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

@Mapper
public interface UserMapper {
    @Select("SELECT * FROM user WHERE username = #{username}")
    User findByUsername(String username);

    @Insert("INSERT INTO user (username, password, email, create_time) VALUES (#{username}, #{password}, #{email}, NOW())")
    int register(User user);
}