package com.example.sys.repository;

import com.example.sys.entity.Favorite;
import com.example.sys.entity.User;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

public interface FavoriteRepository extends JpaRepository<Favorite, Long> {
    Page<Favorite> findByUserOrderByCollectTimeDesc(User user, Pageable pageable);
    boolean existsByUserAndProductId(User user, String productId);
} 