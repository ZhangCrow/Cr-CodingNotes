# PlantWaterDoc
<!--我想涨薪跳槽当老板！！！-->
## 设计文档

### 主要功能
* 自动监测土壤湿度，超过一定干燥值就自动浇水。
* 自动监测水箱水量，水箱水量偏少则暂停土壤湿度监测，且若非深夜则持续蜂鸣。
* 自动监测水箱水量，水量充足则继续土壤湿度监测并停止蜂鸣。

### 硬件需求
已有: microbit主板、扩展板、土壤湿度传感器、水流传感器、环境光传感器、继电器
缺少: 电源电池、水泵
需自制: 水箱

### 硬件方案
通过环境光传感器判断两脚兽是否已熄灯休息
在水箱底部高于水泵进水口的位置放置水流传感器
但是不确定静止的水中水流传感器会获取到怎么样的值

### 代码思路
Pseudocode
```
def main():
	while True:
		is_enough_water = value_from.water_sensor
		is_still_up = value_from.ambient_light_sensor
		if is_enough_water:
			# 水量充足 停止蜂鸣 监测土壤
			music.stop(pin = buzzer)
			need_water = track_soil_humility()
			if need_water:
                watering()
		elif is_still_up:
			# 水量不足&非夜间 蜂鸣提醒两脚兽加水
			music.play（MUSIC_XXX，pin = buzzer，wait = False，loop = True ）
		else:
			# 水量不足&夜间 休眠3h
			sleep(1000*60*60*3)

def track_soil_humility():
	# 这个函数来读取土壤湿度 返回是否需要浇水
	return

def watering():
	# 控制继电器开关水泵
	return

main()

```


