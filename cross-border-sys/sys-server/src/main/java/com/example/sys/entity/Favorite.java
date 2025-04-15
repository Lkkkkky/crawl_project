package com.example.sys.entity;

import lombok.Data;
import javax.persistence.*;
import java.time.LocalDateTime;

@Data
@Entity
@Table(name = "favorites")
public class Favorite {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @ManyToOne
    @JoinColumn(name = "user_id")
    private User user;
    
    @Column(name = "product_id")
    private String productId;
    
    @Column(name = "collect_time")
    private LocalDateTime collectTime;
    
    @Transient
    private Product product;
} 