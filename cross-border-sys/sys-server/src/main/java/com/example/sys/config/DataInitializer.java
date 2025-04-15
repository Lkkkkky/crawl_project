package com.example.sys.config;

import com.example.sys.entity.Product;
import com.example.sys.repository.ProductRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import java.math.BigDecimal;
import java.util.Arrays;

@Component
@RequiredArgsConstructor
public class DataInitializer implements CommandLineRunner {

    private final ProductRepository productRepository;

    @Override
    public void run(String... args) {
        if (productRepository.count() == 0) {
            Product p1 = new Product();
            p1.setName("iPhone 13");
            p1.setPrice(new BigDecimal("5999"));
            p1.setPlatform("Apple");
            p1.setLink("https://www.apple.com");

            Product p2 = new Product();
            p2.setName("MacBook Pro");
            p2.setPrice(new BigDecimal("12999"));
            p2.setPlatform("Apple");
            p2.setLink("https://www.apple.com");

            Product p3 = new Product();
            p3.setName("AirPods Pro");
            p3.setPrice(new BigDecimal("1999"));
            p3.setPlatform("Apple");
            p3.setLink("https://www.apple.com");

            productRepository.saveAll(Arrays.asList(p1, p2, p3));
        }
    }
} 