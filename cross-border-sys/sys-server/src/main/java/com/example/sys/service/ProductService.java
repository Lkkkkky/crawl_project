package com.example.sys.service;

import com.example.sys.entity.Product;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageImpl;
import org.springframework.data.domain.Pageable;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ProductService {
    private static final Logger logger = LoggerFactory.getLogger(ProductService.class);
    private final JdbcTemplate jdbcTemplate;

    public ProductService(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
        logger.info("ProductService initialized");
    }

    public Page<Product> searchProducts(String query, Pageable pageable) {
        logger.debug("Searching products with query: {}", query);
        String sql = "SELECT id, name, price, platform, link FROM goods.products WHERE name LIKE ?";
        try {
            List<Product> products = jdbcTemplate.query(
                sql,
                new Object[]{"%" + query + "%"},
                (rs, rowNum) -> {
                    Product product = new Product();
                    product.setId(rs.getString("id"));
                    product.setName(rs.getString("name"));
                    product.setPrice(rs.getBigDecimal("price"));
                    product.setPlatform(rs.getString("platform"));
                    product.setLink(rs.getString("link"));
                    return product;
                }
            );
            
            int start = (int) pageable.getOffset();
            int end = Math.min((start + pageable.getPageSize()), products.size());
            
            return new PageImpl<>(
                products.subList(start, end),
                pageable,
                products.size()
            );
        } catch (Exception e) {
            logger.error("Error searching products: ", e);
            throw e;
        }
    }

    public Product getProduct(String id) {
        String sql = "SELECT id, name, price, platform, link FROM goods.products WHERE id = ?";
        List<Product> products = jdbcTemplate.query(
            sql,
            new Object[]{id},
            (rs, rowNum) -> {
                Product product = new Product();
                product.setId(rs.getString("id"));
                product.setName(rs.getString("name"));
                product.setPrice(rs.getBigDecimal("price"));
                product.setPlatform(rs.getString("platform"));
                product.setLink(rs.getString("link"));
                return product;
            }
        );
        
        if (products.isEmpty()) {
            throw new RuntimeException("Product not found");
        }
        
        return products.get(0);
    }
} 