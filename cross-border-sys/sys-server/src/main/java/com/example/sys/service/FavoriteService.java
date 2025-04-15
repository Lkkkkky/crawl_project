package com.example.sys.service;

import com.example.sys.entity.Favorite;
import com.example.sys.entity.Product;
import com.example.sys.entity.User;
import com.example.sys.repository.FavoriteRepository;
import com.example.sys.service.ProductService;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;

@Service
@RequiredArgsConstructor
public class FavoriteService {
    private final FavoriteRepository favoriteRepository;
    private final ProductService productService;

    public void addFavorite(User user, Product product) {
        if (favoriteRepository.existsByUserAndProductId(user, product.getId())) {
            throw new RuntimeException("Already in favorites");
        }

        Favorite favorite = new Favorite();
        favorite.setUser(user);
        favorite.setProductId(product.getId());
        favorite.setCollectTime(LocalDateTime.now());
        favorite.setProduct(product);
        favoriteRepository.save(favorite);
    }

    public Page<Favorite> getUserFavorites(User user, Pageable pageable) {
        Page<Favorite> favorites = favoriteRepository.findByUserOrderByCollectTimeDesc(user, pageable);
        // 加载每个收藏对应的商品信息
        favorites.getContent().forEach(favorite -> {
            favorite.setProduct(productService.getProduct(favorite.getProductId()));
        });
        return favorites;
    }

    public void deleteFavorite(Long id, User user) {
        Favorite favorite = favoriteRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Favorite not found"));
        
        if (!favorite.getUser().getId().equals(user.getId())) {
            throw new RuntimeException("Not authorized");
        }
        
        favoriteRepository.delete(favorite);
    }
} 