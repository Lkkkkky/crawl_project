import React, { useState,useEffect } from "react";
import "./Home.css";
// var index=1

var global_data
var display_result
function App() {
  const [query, setQuery] = useState(""); //用户输入的关键词
  const [results, setResults] = useState([]);// 当前展示的数据
  const [data, setData] = useState([]); // 本地存储的所有数据
  const [currentPage, setCurrentPage] = useState(0); // 当前页码
  const [totalPages, setTotalPages] = useState(0); // 总页数
  const [loading, setLoading] = useState(false); // 数据加载状态
  const [index, setIndex] = useState(1); // 数据加载状态
  const itemsPerPage = 10; // 每页显示的条数
  var index_
  let isFetching = false;


  useEffect(() => {
        console.log("totalPages 已更新为:",currentPage);
        // if(currentPage===2)
        if (currentPage===1){
          callPythonAPI()
          // handlePageChange(currentPage-1)
        }
        else
        {
          handlePageChange(currentPage-1)
        }

    }, [currentPage]);  // 依赖于 setCurrentPage，状态更新时触发

function callPythonAPI() {
    //标识已爬取过，翻到第一页的时候不再爬取

       if (isFetching) return; // 防止重复点击
    isFetching = true;
    setLoading(true);
    const keyword = document.getElementById('searchInput').value;
    console.log(keyword)
    fetch(`http://127.0.0.1:5000/run-python?keyword=${encodeURIComponent(keyword)}`)
        .then(response => response.json())
        .then(result_data => {
            console.log('Response from Python:', result_data);
            global_data=result_data
            // global_data=Object.values(result_data['data'])
            setTotalPages(parseInt(global_data.length/itemsPerPage))
            display_result=getCurrentPageData(result_data) //获取当前页面的数据
            populateTable(display_result);//初始化展示的数据

        })
        .catch(error => {
            console.error('Error:', error);
        })
        .finally(() => {
            setLoading(false);
            isFetching = false; // 允许再次点击
        });

}

    //获取当前页的数据
  const getCurrentPageData = (data) => {
    // var data_ = Object.values(data)
    var data_ = data
    const startIndex = (currentPage - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;
    console.log(data_.slice(startIndex, endIndex))
    return data_.slice(startIndex, endIndex);

  }
   // 处理翻页逻辑
   const handlePageChange = async (page) => {

    // 如果请求的页码超出已加载数据范围

     display_result=global_data.slice((page-1)*10,(page-1)*10+itemsPerPage);
     console.log(display_result);
     populateTable(display_result);
     // populateTable(new_data)
  };
  //更新表格
  function populateTable(data) {
    // 获取表格主体部分
    const tableBody = document.getElementById('resultsTable').getElementsByTagName('tbody')[0];
    index_=(currentPage-1)*10+1
    // 清空现有的表格数据
    tableBody.innerHTML = '';


      // 遍历字典并将每个产品信息插入表格
      for ( let i =0; i < data.length; i++) {
        var good = data[i]
          const product = good['good_name'];
          const good_price = good['good_price'];
          const url = good['good_url'];
          const source = good['good_source'];

          // 创建一行数据
          let row = tableBody.insertRow();

          // 创建单元格并填充数据
          let cell0 = row.insertCell(0); // 索引
          cell0.textContent = index_;
          index_=index_+1
          let cell1 = row.insertCell(1); // 商品名称
          cell1.textContent = product; // 使用字典的键（产品ID）

          let cell2 = row.insertCell(2);// 商品价格
          if(good_price){cell2.textContent = good_price;}else{cell2.textContent = '暂无价格';}


          let cell3 = row.insertCell(3);
          let link = document.createElement("a"); // 商品链接
          link.href = url;  // 设置超链接地址
          link.textContent = "商品链接";  // 设置超链接文本
          link.target = "_blank";  // 设置为在新标签页打开链接
          cell3.appendChild(link);  // 将超链接添加到单元格中

          let cell4 = row.insertCell(4); // 商品来源
          cell4.textContent = source;

     }

  }

  // 搜索商品（模拟接口请求）
  const searchProducts = async () => {
    // 模拟 API 数据返回
    const data = Array.from({ length: 10 }, (_, index) => ({
      id: index + 1,
      name: `搜索结果商品 ${index + 1}`,
      price: (Math.random() * 100).toFixed(2),
      link: "https://example.com",
    }));
    setResults(data);
  };


  // 使用结果数据或默认数据
  // const displayData = results.length > 0 ? results : defaultData;

  return (
    <div className="App">
      {/* 顶部导航 */}
      <header>
        <h1>商品比价系统</h1>
        <div className="search-bar">
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="搜索商品..."
            id="searchInput"
          />
          <button onClick={() => {
            setCurrentPage(1)

          }}>搜索</button>
        </div>
      </header>

      {/* 商品列表 */}
      <div className="table-container">
        <table id="resultsTable">
          <thead>
            <tr>
              <th>序号</th>
              <th>商品名称</th>
              <th>价格</th>
              <th>商品链接</th>
              <th>来源平台</th>
            </tr>
          </thead>
          <tbody>
            {/*{getCurrentPageData().map((item, index) => (*/}
            {/*  <tr key={index}>*/}
            {/*    <td>{index + 1}</td>*/}
            {/*    <td>{item.name}</td>*/}
            {/*    <td>￥{item.price}</td>*/}
            {/*    <td>*/}
            {/*      <a href={item.link} target="_blank" rel="noopener noreferrer">*/}
            {/*        查看商品*/}
            {/*      </a>*/}
            {/*    </td>*/}
            {/*  </tr>*/}
            {/*))}*/}
          </tbody>
        </table>
      </div>
      {/* 分页导航 */}
      <div className="pagination">
        <button
          onClick={() => {

            setCurrentPage(currentPage-1)

          }
        }
          disabled={currentPage === 1}
        >
          上一页
        </button>
        <span>
          页码 {currentPage} / {totalPages}
        </span>
        <button
          onClick={() =>
          {

            setCurrentPage(currentPage+1)


          }
          }
          disabled={loading}
          disabled={currentPage===totalPages}
        >
          下一页
        </button>
        <input
          type="number"
          min="1"
          max={totalPages}
          placeholder="跳转页码"
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              const page = parseInt(e.target.value, 10);
              if (!isNaN(page) && page >= 1 && page <= totalPages) {
                handlePageChange(page);
              }
            }
          }}
        />
      </div>
      {/* 页脚 */}
      <footer>
        <p>© 2024 商品比价系统</p>
      </footer>
    </div>
  );
}

export default App;
