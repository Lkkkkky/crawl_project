CREATE TABLE IF NOT EXISTS recommendations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL COMMENT '用户账号',
    good_name VARCHAR(255) NOT NULL COMMENT '商品名称',
    good_url VARCHAR(500) NOT NULL COMMENT '商品链接',

    good_source VARCHAR(50) COMMENT '来源平台',
    similarity_score FLOAT NOT NULL COMMENT '相似度分数',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    INDEX idx_username (username),
    INDEX idx_good_url (good_url(255)),
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='推荐商品表';