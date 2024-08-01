## 什么是Milvus
>Milvus 创建于 2019 年，其唯一目标是：存储、索引和管理由深度神经网络和其他机器学习 (ML) 模型生成的大量[嵌入向量。](https://milvus.io/docs/overview.md#Embedding-vectors)
>
>作为一款专为处理向量查询而设计的数据库，Milvus 能够对万亿级向量进行索引。与现有的主要处理按照预定义模式进行结构化数据的关系型数据库不同，Milvus 自下而上地设计用于处理从非结构化数据转换而来的嵌入[向量](https://milvus.io/docs/overview.md#Unstructured-data)。
>
>随着互联网的发展，非结构化数据变得越来越普遍，包括电子邮件、论文、物联网传感器数据、Facebook 照片、蛋白质结构等等。为了让计算机理解和处理非结构化数据，需要使用嵌入技术将这些数据转换为向量。Milvus 存储并索引这些向量。Milvus 能够通过计算相似性距离来分析两个向量之间的相关性。如果两个嵌入向量非常相似，则意味着原始数据源也相似。

## 相关概念文档

- [Milvus 词汇表](https://milvus.io/docs/glossary.md)。
### 非结构化数据

非结构化数据（包括图像、视频、音频和自然语言）是不遵循预定义模型或组织方式的信息。此类数据约占全球数据的 80%，可以使用各种人工智能 (AI) 和机器学习 (ML) 模型将其转换为向量。
### 嵌入向量

嵌入向量是非结构化数据（例如电子邮件、物联网传感器数据、Instagram 照片、蛋白质结构等）的特征抽象。从数学上讲，嵌入向量是浮点数或二进制数组。现代嵌入技术用于将非结构化数据转换为嵌入向量。
### 向量相似性搜索

向量相似性搜索是将向量与数据库进行比较以找到与查询向量最相似的向量的过程。近似最近邻 (ANN) 搜索算法用于加速搜索过程。如果两个嵌入向量非常相似，则意味着原始数据源也相似。
## 支持的指数和指标

>索引是数据的组织单位，在搜索或查询插入实体之前，必须声明索引类型和相似度指标。**如果不指定索引类型，Milvus 默认会进行暴力搜索**
### 索引类型
[向量索引](https://milvus.io/docs/index.md)。
Milvus 支持的向量索引类型大部分都采用了近似最近邻搜索（ANNS），具体包括：

- **HNSW**：HNSW 是基于图的索引，适合对搜索效率要求较高的场景。还有一个 GPU 版本**GPU_CAGRA**
- **FLAT**：FLAT 最适合在百万级小型数据集上寻求完美准确搜索结果的场景。还有一个 GPU 版本**GPU_BRUTE_FORCE**。
- **IVF_FLAT**：IVF_FLAT 是基于量化的索引，最适合在准确率和查询速度之间寻求理想平衡的场景。此外还有 GPU 版本**GPU_IVF_FLAT**。
- **IVF_SQ8**：IVF_SQ8 是一个基于量化的索引，最适合于寻求大幅减少磁盘、CPU 和 GPU 内存消耗的场景，因为这些资源非常有限。
- **IVF_PQ**：IVF_PQ 是基于量化的索引，适合那些追求查询速度，甚至牺牲准确率的场景。另外还有 GPU 版本**GPU_IVF_PQ**。
- **SCANN** : SCANN 在向量聚类和乘积量化方面与 IVF_PQ 类似，不同之处在于乘积量化的实现细节以及使用 SIMD（单指令/多数据）进行高效计算。
- **DiskANN**：基于 Vamana 图表，DiskANN 可在大型数据集内提供高效搜索。

### 相似度指标
[相似度度量](https://milvus.io/docs/metric.md#floating)
在 Milvus 中，相似度度量用于衡量向量之间的相似性。选择一个好的距离度量有助于显著提高分类和聚类性能。根据输入数据形式，选择特定的相似度度量以获得最佳性能。

广泛用于浮点嵌入的指标包括：

- **余弦**：该指标是标准化的IP，一般用于文本相似性搜索（NLP）。
- **欧几里得距离（L2）**：该度量通常用于计算机视觉（CV）领域。
- **内积 (IP)**：该指标通常用于自然语言处理 (NLP) 领域。广泛用于二元嵌入的指标包括：
- **汉明（Hamming**）：该度量通常用于自然语言处理（NLP）领域。
- **Jaccard**：该度量一般用于分子相似性搜索领域。

## Milvus的设计

Milvus 作为云原生矢量数据库，在设计上将存储与计算分离，为增强弹性和灵活性，Milvus 中的所有组件都是无状态的。

该系统分为四个级别：

- 接入层：接入层由一组无状态的代理组成，是系统的前层，也是面向用户的端点。
- 协调器服务：协调器服务将任务分配给工作节点，并充当系统的大脑。
- 工作节点：工作节点充当手臂和腿，是愚蠢的执行者，遵循协调服务的指令并执行用户触发的 DML/DDL 命令。
- 存储：存储是系统的骨架，负责数据的持久化，包括元存储、日志代理、对象存储。

[架构概述](https://milvus.io/docs/architecture_overview.md)
![image-2020240709104044](../后端/云原生/Pasted%20image%2020240709104044.png)
## 安装Milvus
相关参考
Milvus1.0 安装方式可参考以下文档：
- [Docker 安装 Milvus1.0 CPU 版本](https://milvus.io/cn/docs/v1.0.0/milvus_docker-cpu.md)。
- [Docker 安装 Milvus1.0 GPU 版本](https://milvus.io/cn/docs/v1.0.0/milvus_docker-gpu.md)。
- [通过编译源码安装 Milvus1.0](https://github.com/milvus-io/milvus/blob/1.0/INSTALL.md).
- [通过 Mishards 部署 Milvus1.0 分布式版本](https://github.com/milvus-io/bootcamp/tree/master/deployments/Mishards)。
### docker安装
```shell
 # 如果网速不好下载不下来，可以使用浏览器或下载器下载下面的连接，并将文件改名为docker-compose.yml
wget https://github.com/milvus-io/milvus/releases/download/v2.4.5/milvus-standalone-docker-compose.yml -O docker-compose.yml

# 运行 视情况加sudo
docker compose up -d

# 成功后大概如下
# Creating milvus-etcd ... done 
# Creating milvus-minio ... done 
# Creating milvus-standalone ... done
```
- 在docker desktop中查看containers
- ![image-20240709104447](../后端/云原生/Pasted%20image%2020240709104447.png)
- 在终端检查
```shell
❯ docker ps
CONTAINER ID   IMAGE                                      COMMAND                  CREATED          STATUS                    PORTS                                              NAMES
16ebbc9a0b6a   milvusdb/milvus:v2.4.5                     "/tini -- milvus run…"   46 minutes ago   Up 46 minutes (healthy)   0.0.0.0:9091->9091/tcp, 0.0.0.0:19530->19530/tcp   milvus-standalone
2120c3e579a2   minio/minio:RELEASE.2023-03-20T20-16-18Z   "/usr/bin/docker-ent…"   46 minutes ago   Up 46 minutes (healthy)   0.0.0.0:9000-9001->9000-9001/tcp                   milvus-minio
9874879a134b   quay.io/coreos/etcd:v3.5.5                 "etcd -advertise-cli…"   46 minutes ago   Up 46 minutes (healthy)   2379-2380/tcp   
```

### 使用pymilvus进行测试学习
python >= 3.8+
```bash
# 安装pymilvus
pip install -U pymilvus
# 安装模型库
pip install "pymilvus[model]"
```
#### 创建数据库
要创建本地 Milvus 矢量数据库，只需`MilvusClient`通过指定一个文件名来实例化一个来存储所有数据，例如“my_demo.db”。
```python
from pymilvus import MilvusClient

client = MilvusClient("my_demo.db")
```
#### 创建收藏夹
在milvus中，向量的元数据和存储是通过集合进行存储，类似传统SQL数据库中的表（Table）。创建集合时，定义schema和index配置向量的规格：维度、索引类型、距离度量。
```python
if client.has_collection(collection_name="demo_test"):
	client.drop_collection(collection_name="demo_test")
client.create_collection(
	collection_name="demo_test",
	dimension=768, # 向量有768维度
)
```
#### 准备数据
使用默认模型生成向量嵌入。Milvus 要求数据以字典列表的形式插入，其中每个字典代表一条数据记录，称为实体。
```python
from pymilvus import model

embedding_fn = model.DefaultEmbeddingFunction()

# 要搜索的文本字符串。
docs = [
	"人工智能于1956年作为一门学科成立。",
	"艾伦·图灵是第一个对人工智能进行实质性研究的人。",
	"图灵出生在伦敦的Maida Vale，在英格兰南部长大。",
]

vectors = embedding_fn.encode_documents(docs)
data = [
	{"id": 3 + i, "vector": vectors[i], "text": docs[i], "subject": "biology"}
	for i in range(len(vectors))
]

print("数据包含", len(data), "实体, 其中有字段: ", data[0].keys())
```
```bash
数据包含 3 实体, 其中有字段:  dict_keys(['id', 'vector', 'text', 'subject'])
```
#### 插入数据
```python
client.insert(collection_name="demo_test", data=data)
```
#### 语义搜索
```python
res = client.search(
	collection_name="demo_test",
	data=embedding_fn.encode_queries(["谁在英格兰南部长大"]),
	filter="subject == 'biology'",
	limit=2,
	output_fields=["text", "subject"],
)
print(res)
```
#### 完整代码
```python
import random
from pymilvus import MilvusClient
from pymilvus import model

client = MilvusClient("my_demo.db")

embedding_fn = model.DefaultEmbeddingFunction()

if client.has_collection(collection_name="demo_test"):
	client.drop_collection(collection_name="demo_test")
client.create_collection(
	collection_name="demo_test",
	dimension=768, 
)

docs = [
	"人工智能于1956年作为一门学科成立。",
	"艾伦·图灵是第一个对人工智能进行实质性研究的人。",
	"图灵出生在伦敦的Maida Vale，在英格兰南部长大。",
]

vectors = embedding_fn.encode_documents(docs)

data = [
	{"id": 3 + i, "vector": vectors[i], "text": docs[i], "subject": "biology"}
	for i in range(len(vectors))
]

client.insert(collection_name="demo_test", data=data)

print("数据包含", len(data), "实体, 其中有字段: ", data[0].keys())

res = client.search(
	collection_name="demo_test",
	data=embedding_fn.encode_queries(["谁在英格兰南部长大"]),
	limit=2,
	output_fields=["text", "subject"],
)
print(res)
```

```bash
数据包含 3 实体, 其中有字段:  dict_keys(['id', 'vector', 'text', 'subject'])
data: ["[{'id': 4, 'distance': 1.0, 'entity': {'text': '艾伦·图灵是第一个对人工智能进行实质性研究的人。', 'subject': 'biology'}}, {'id': 5, 'distance': 0.34042733907699585, 'entity': {'text': '图灵出生在伦敦的Maida Vale，在英格兰南部长大。', 'subject': 'biology'}}]"] , extra_info: {'cost': 0}
```
#### 带元数据过滤的向量搜索
插入几条新数据
```python
docs = [
	"机器学习已经被用于药物设计。",
	"用人工智能算法计算合成预测分子性质。",
	"DDR1参与癌症和纤维化。"
]
vectors = embedding_fn.encode_documents(docs)
data = [ 
	{"id": 3 + i, "vector": vectors[i], "text": docs[i], "subject": "newSubject"} 
	for i in range(len(vectors)) 
]
client.insert(collection_name="demo_test", data=data)
print("数据包含", len(data), "实体, 其中有字段: ", data[0].keys())
```
搜索subject == 'newSubject'
```python
res = client.search(
	collection_name="demo_test",
	data=embedding_fn.encode_queries(["人工智能的相关信息"]),
	filter="subject == 'newSubject'",
	limit=2,
	output_fields=["text", "subject"],
)
```
输出结果
```bash
data: ["[{'id': 4, 'distance': 1.0, 'entity': {'text': '用人工智能算法计算合成预测分子性质。', 'subject': 'newSubject'}}, {'id': 3, 'distance': 1.0, 'entity': {'text': '机器学习已经被用于药物设计。', 'subject': 'newSubject'}}]"] , extra_info: {'cost': 0}
```
结果输出中，只包含了subject == 'newSubject'的数据，如果需要在大型数据集中执行元数据过滤搜索，可以考虑使用固定架构并开启索引提高搜索性能。
#### query() 
query方法是一种检索与凭据匹配的所有实体的操作

例如：检索某些特征值
```python
res = client.query(
    collection_name="demo_test",
    filter="subject == 'history'",
    output_fields=["text", "subject"],
)
```
例如：直接搜索主键
```python
res = client.query(
    collection_name="demo_test",
    ids=[0, 2],
    output_fields=["vector", "text", "subject"],
)
```
#### 删除实体
删除指定主键的实体或删除与特定过滤表达式匹配的所有实体
```python
res = client.delete(collection_name="demo_test", ids=[0, 2])

print(res)

res = client.delete(
    collection_name="demo_test",
    filter="subject == 'newSubject'",
)

print(res)

```

```bash
[0, 2] 
[3, 4, 5]
```
#### 删除集合
类似删表
```python
client.drop_collection(collection_name="demo_test")
```
## 安装Attu图形工具

>https://github.com/zilliztech/attu/releases
>选择自己需要的相关版本下载

- ![image-20240709112926](../后端/云原生/Pasted%20image%2020240709112926.png)
输入docker地址进入
- ![image-20240709112948](../后端/云原生/Pasted%20image%2020240709112948.png)

怎么用就不记录了，详细参考github[https://github.com/zilliztech/attu/blob/main/doc/zh-cn.md]


