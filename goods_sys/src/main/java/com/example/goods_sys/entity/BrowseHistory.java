package com.example.goods_sys.entity;

import lombok.Data;
import java.util.Date;

@Data
public class BrowseHistory {
    private String good_url;
    private String good_name;
    private String good_price;
    private String good_source;
    private Date browse_time;
}