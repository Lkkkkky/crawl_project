package com.example.sys.service;

import com.example.sys.entity.History;
import com.example.sys.entity.Product;
import com.example.sys.entity.User;
import com.example.sys.repository.HistoryRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;

@Service
@RequiredArgsConstructor
public class HistoryService {
    private final HistoryRepository historyRepository;

    public void addHistory(User user, Product product) {
        History history = new History();
        history.setUser(user);
        history.setProduct(product);
        history.setViewTime(LocalDateTime.now());
        historyRepository.save(history);
    }

    public Page<History> getUserHistory(User user, Pageable pageable) {
        return historyRepository.findByUserOrderByViewTimeDesc(user, pageable);
    }

    public void deleteHistory(Long id, User user) {
        History history = historyRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("History not found"));
        
        if (!history.getUser().getId().equals(user.getId())) {
            throw new RuntimeException("Not authorized");
        }
        
        historyRepository.delete(history);
    }
} 