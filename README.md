# Crypto API Server | 加密货币数据 API 服务

A FastAPI-based backend that provides real-time cryptocurrency metrics and prices, including:
基于 FastAPI 构建的后端服务，提供以下加密货币相关实时数据：

## ✅ Features | 功能

- 📊 BTC Dominance（BTC 占有率）
- 😱 Fear & Greed Index（恐惧与贪婪指数）
- 🧾 BTC Options (from Binance)（BTC 期权数据 - 来自币安）
- 💰 BTC Prices from Multiple Exchanges（多交易所 BTC 现货价格）

---

## 🚀 Deployment on Render | 在 Render 上部署

### Option 1: Deploy from GitHub | 从 GitHub 部署

1. Push this project to your GitHub repo
2. Go to [https://render.com](https://render.com)
3. Click **"New Web Service"**
4. Select your repo
5. Set Environment as: **Docker**
6. No build/start command needed
7. Port: **8000**

### Option 2: Local Docker (Optional) | 本地部署（可选）

```bash
docker build -t crypto-api .
docker run -p 8000:8000 crypto-api
```

---

## 🛠️ API Endpoints | API 接口

| Endpoint                | Description                  | 描述                         |
|------------------------|------------------------------|------------------------------|
| `/btc-dominance`       | BTC Dominance %              | BTC 占比                     |
| `/fear-greed`          | Fear & Greed Index           | 恐惧与贪婪指数               |
| `/btc-options`         | BTC Options from Binance     | 币安 BTC 期权数据            |
| `/btc-prices`          | BTC Spot Prices (multi-exchange) | 多交易所现货价格          |

---

## 🌐 Example Frontend Call | 前端调用示例（Next.js）

```tsx
useEffect(() => {
  fetch("https://your-app.onrender.com/btc-prices")
    .then(res => res.json())
    .then(console.log)
}, []);
```

---

## 📂 Project Structure | 项目结构

```
crypto_api/
├── main.py                  # FastAPI app entry
├── services/                # Service modules
│   ├── btc_dominance.py    # BTC 占有率
│   ├── fear_greed.py       # 恐惧与贪婪指数
│   ├── options.py          # 期权数据
│   └── prices.py           # 多交易所现货价格
├── Dockerfile              # Docker 容器配置
├── requirements.txt        # Python 依赖
```

---

## 📧 Contact / 联系方式

If you have questions or want to contribute, feel free to open an issue or PR!  
如需反馈或贡献代码，欢迎提交 issue 或 PR。

---

MIT License © 2025
