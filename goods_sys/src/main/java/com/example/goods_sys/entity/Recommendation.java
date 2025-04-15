package com.example.goods_sys.entity;

import lombok.Data;
import java.util.Date;

@Data
public class Recommendation {
    private String username;
    private String good_url;
    private String good_name;
    private String good_source;
    private Double similarity_score;
    private Date recommend_time;
}