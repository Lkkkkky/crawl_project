package com.example.sys.repository;

import com.example.sys.entity.History;
import com.example.sys.entity.User;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

public interface HistoryRepository extends JpaRepository<History, Long> {
    Page<History> findByUserOrderByViewTimeDesc(User user, Pageable pageable);
} 