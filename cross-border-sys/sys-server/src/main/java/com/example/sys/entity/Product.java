package com.example.sys.entity;

import lombok.Data;
import javax.persistence.*;
import java.math.BigDecimal;

@Data
public class Product {
    private String id;
    
    private String name;
    
    private BigDecimal price;
    
    private String link;
    
    private String platform;
} 