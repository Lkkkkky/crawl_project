# 导入FastAPI相关的核心组件
from fastapi import FastAPI, HTTPException, Depends, status
# 导入SQLAlchemy ORM相关组件
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
# 导入日期时间处理相关模块
from datetime import datetime
# 导入类型提示相关模块
from typing import List
# 导入Pydantic数据验证模块
from pydantic import BaseModel
# 导入ASGI服务器
import uvicorn

# 创建FastAPI应用实例，设置API文档信息
app = FastAPI(
    title="FastAPI入门示例",
    description="一个简单的FastAPI后端接口示例，适合初学者学习",
    version="1.0.0",
    docs_url="/docs",  # 启用API文档路由
    redoc_url="/redoc"  # 启用ReDoc文档路由
)

# 配置SQLite数据库连接
DATABASE_URL = "sqlite:///./test.db"
# 创建数据库引擎实例
engine = create_engine(DATABASE_URL)
# 创建数据库会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 创建声明性基类
Base = declarative_base()

# 定义用户数据模型
class User(Base):
    __tablename__ = "users"  # 指定数据库表名
    # 定义表字段
    id = Column(Integer, primary_key=True, index=True)  # 主键字段
    username = Column(String, unique=True, index=True)  # 用户名字段，唯一且建立索引
    email = Column(String, unique=True, index=True)  # 邮箱字段，唯一且建立索引
    password = Column(String)  # 密码字段
    created_at = Column(DateTime, default=datetime.utcnow)  # 创建时间字段

class Good(Base):
    __tablename__ = "goods"  # 指定数据库表名
    # 定义表字段
    id = Column(Integer, primary_key=True, index=True)  # 主键字段
    goodname = Column(String, unique=True, index=True)  # 用户名字段，唯一且建立索引
    price = Column(String, unique=True, index=True)  # 邮箱字段，唯一且建立索引
    stock = Column(String)  # 密码字段
    created_at = Column(DateTime, default=datetime.utcnow)  # 创建时间字段

class GoodBase(BaseModel):
    goodname: str  # 
    

class GoodCreate(GoodBase):
    stock: str  #
    price: str  # 

class GoodsResponse(GoodBase):
    id: int  # 用户ID字段
    goodname:str
    created_at: datetime  # 创建时间字段
    class Config:
        from_attributes = True  # 更新为新版本的配置项


# 定义用户基础Pydantic模型
class UserBase(BaseModel):
    username: str  # 用户名字段
    email: str  # 邮箱字段

# 定义用户创建请求模型
class UserCreate(UserBase):
    password: str  # 密码字段

# 定义用户响应模型
class UserResponse(UserBase):
    id: int  # 用户ID字段
    created_at: datetime  # 创建时间字段

    class Config:
        from_attributes = True  # 更新为新版本的配置项

# 定义数据库会话依赖
def get_db():
    """创建数据库会话的依赖函数"""
    db = SessionLocal()  # 创建新的数据库会话
    try:
        yield db  # 返回数据库会话
    finally:
        db.close()  # 确保会话被关闭

# API路由定义
@app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """创建新用户的API端点"""
    # 检查用户名是否已存在
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="用户名已被注册")
    
    # 创建新用户实例
    db_user = User(
        username=user.username,
        email=user.email,
        password=user.password  # 注意：实际应用中应该对密码进行加密处理
    )
    # 将新用户添加到数据库
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
@app.post("/goods_add", response_model=GoodsResponse, status_code=status.HTTP_201_CREATED)
async def create_good(good: GoodCreate, db: Session = Depends(get_db)):
    """创建新用户的API端点"""
    # 检查用户名是否已存在
    db_good = db.query(Good).filter(Good.goodname == good.goodname).first()
    if db_good:
        raise HTTPException(status_code=400, detail="用户名已被注册")
    
    # 创建新用户实例
    db_good = Good(
        goodname=good.goodname,
        stock=good.stock, #
        price=good.price,
        
       
    )
    # 将新用户添加到数据库
    db.add(db_good)
    db.commit()
    db.refresh(db_good)
    return db_good
@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    """获取指定用户信息的API端点"""
    # 查询指定ID的用户
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="用户不存在")
    return db_user

@app.get("/users/", response_model=List[UserResponse])
async def list_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """获取用户列表的API端点"""
    # 查询用户列表，支持分页
    users = db.query(User).offset(skip).limit(limit).all()
    return users

# 主程序入口
if __name__ == "__main__":
    # 创建数据库表
    Base.metadata.create_all(bind=engine)
    
    # 启动FastAPI应用服务器
    uvicorn.run(
        "main:app",  # 应用实例的导入路径
        host="127.0.0.1",  # 监听本地网络接口
        port=8000,  # 服务端口
        reload=True  # 启用热重载
    )