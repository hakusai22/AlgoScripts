package config_test

import (
	"fmt"
	"github.com/fsnotify/fsnotify"
	"github.com/spf13/viper"
)

/*
    @Author  : https://github.com/hakusai22
    @Time    : 2024/08/04 18:26
    @题目     :
    @参考     :
    @时间复杂度:
    @空间复杂度:

 数据范围:

*/

func configRead() {
	//配置项: ContentDir 默认值: content
	viper.SetDefault("ContentDir", "content")
	viper.SetConfigName("config")         // 配置文件名称(无扩展名)
	viper.SetConfigFile("./config.yaml")  // 指定配置文件路径
	viper.SetConfigType("yaml")           // 如果配置文件的名称中没有扩展名，则需要指定
	viper.AddConfigPath("/etc/appname/")  // 查找配置文件所在的路径
	viper.AddConfigPath("$HOME/.appname") // 多次调用可以多次搜索路径
	viper.AddConfigPath(".")              // 选择性的在工作目录中查找配置
	// 处理找不到配置文件的情况
	err := viper.ReadInConfig()
	if err != nil {
		panic(fmt.Errorf("Fatal error config file: %s \n", err))
	}

	//  将当前 viper 配置写入预定义的路径（如果存在）。如果没有预定义的路径，将报错。如果配置文件已经存在则将覆盖当前配置文件。
	viper.WriteConfig()
	//  和WriteConfig类似只是不会覆盖
	viper.SafeWriteConfig()
	//
	viper.WriteConfigAs("/path/to/my/.config")
	viper.SafeWriteConfigAs("/path/to/my/.config")
	viper.SafeWriteConfigAs("/path/to/my/.other_config")

	//监听变化
	viper.WatchConfig()
	// 变动之后的回调
	viper.OnConfigChange(func(e fsnotify.Event) {
		fmt.Println("Config file changed:", e.Name)
	})

	// etcd
	viper.AddRemoteProvider("etcd", "http://127.0.0.1:4001", "/config/hugo.json")
	viper.SetConfigType("json") // 因为字节流中没有扩展名，需要设置，支持的扩展名为:"json", "toml", "yaml", "yml", "properties", "props", "prop", "env", "dotenv"
	err = viper.ReadRemoteConfig()

	// etcd3
	viper.AddRemoteProvider("etcd3", "http://127.0.0.1:4001", "/config/hugo.json")
	viper.SetConfigType("json") // 因为字节流中没有扩展名，需要设置，支持的扩展名为:"json", "toml", "yaml", "yml", "properties", "props", "prop", "env", "dotenv"
	err = viper.ReadRemoteConfig()

	// consul
	viper.AddRemoteProvider("consul", "localhost:8500", "MY_CONSUL_KEY")
	viper.SetConfigType("json") // 需要显式设置成格式'json'
	err = viper.ReadRemoteConfig()

	fmt.Println(viper.Get("port"))     // 8080
	fmt.Println(viper.Get("hostname")) // myhostname.com

	//firestore
	viper.AddRemoteProvider("firestore", "google-cloud-project-id", "collection/document")
	viper.SetConfigType("json") // 配置格式: "json", "toml", "yaml", "yml"
	err = viper.ReadRemoteConfig()

}
