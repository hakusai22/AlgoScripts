module Go_Study

//module: 用于定义当前项目的模块路径
//go:标识当前Go版本.即初始化版本
go 1.21

// indirect: 示该模块为间接依赖，也就是在当前应用程序中的 import 语句中，并没有发现这个模块的明确引用
// require: 当前项目依赖的一个特定的必须版本
require github.com/emirpasic/gods v1.18.1

require (
	github.com/aws/aws-sdk-go v1.54.20
	github.com/emersion/go-imap v1.2.1
	github.com/emersion/go-message v0.18.1
	github.com/emirpasic/gods/v2 v2.0.0-alpha
	github.com/fsnotify/fsnotify v1.7.0
	github.com/go-ego/gse v0.80.2
	github.com/gorilla/mux v1.8.1
	github.com/gorilla/websocket v1.5.3
	github.com/mkevac/debugcharts v0.0.0-20191222103121-ae1c48aa8615
	github.com/panjf2000/ants/v2 v2.10.0
	github.com/sashabaranov/go-openai v1.26.3
	github.com/spf13/viper v1.19.0
	github.com/tealeg/xlsx v1.0.5
)

require (
	github.com/StackExchange/wmi v0.0.0-20190523213315-cbe66965904d // indirect
	github.com/emersion/go-sasl v0.0.0-20200509203442-7bfe0ed36a21 // indirect
	github.com/go-ole/go-ole v1.2.4 // indirect
	github.com/hashicorp/hcl v1.0.0 // indirect
	github.com/jmespath/go-jmespath v0.4.0 // indirect
	github.com/magiconair/properties v1.8.7 // indirect
	github.com/mitchellh/mapstructure v1.5.0 // indirect
	github.com/pelletier/go-toml/v2 v2.2.2 // indirect
	github.com/sagikazarmark/locafero v0.4.0 // indirect
	github.com/sagikazarmark/slog-shim v0.1.0 // indirect
	github.com/shirou/gopsutil v2.19.11+incompatible // indirect
	github.com/shirou/w32 v0.0.0-20160930032740-bb4de0191aa4 // indirect
	github.com/sourcegraph/conc v0.3.0 // indirect
	github.com/spf13/afero v1.11.0 // indirect
	github.com/spf13/cast v1.6.0 // indirect
	github.com/spf13/pflag v1.0.5 // indirect
	github.com/subosito/gotenv v1.6.0 // indirect
	github.com/vcaesar/cedar v0.20.1 // indirect
	go.uber.org/atomic v1.9.0 // indirect
	go.uber.org/multierr v1.9.0 // indirect
	golang.org/x/exp v0.0.0-20230905200255-921286631fa9 // indirect
	golang.org/x/sync v0.7.0 // indirect
	golang.org/x/sys v0.18.0 // indirect
	golang.org/x/text v0.14.0 // indirect
	gopkg.in/ini.v1 v1.67.0 // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
)
