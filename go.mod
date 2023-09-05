module Go_Study

//module: 用于定义当前项目的模块路径
//go:标识当前Go版本.即初始化版本
go 1.18

// indirect: 示该模块为间接依赖，也就是在当前应用程序中的 import 语句中，并没有发现这个模块的明确引用
// require: 当前项目依赖的一个特定的必须版本
require (
	github.com/emirpasic/gods v1.18.1
	github.com/garyburd/redigo v1.6.4
	github.com/gin-gonic/gin v1.9.1
	github.com/go-sql-driver/mysql v1.7.1
	github.com/gorilla/websocket v1.5.0
	github.com/natefinch/lumberjack v2.0.0+incompatible
	github.com/roylee0704/gron v0.0.0-20160621042432-e78485adab46
	go.uber.org/zap v1.25.0
)

require (
	github.com/BurntSushi/toml v1.3.2 // indirect
	github.com/bytedance/sonic v1.9.1 // indirect
	github.com/chenzhuoyu/base64x v0.0.0-20221115062448-fe3a3abad311 // indirect
	github.com/gabriel-vasile/mimetype v1.4.2 // indirect
	github.com/gin-contrib/sse v0.1.0 // indirect
	github.com/go-playground/locales v0.14.1 // indirect
	github.com/go-playground/universal-translator v0.18.1 // indirect
	github.com/go-playground/validator/v10 v10.14.0 // indirect
	github.com/goccy/go-json v0.10.2 // indirect
	github.com/json-iterator/go v1.1.12 // indirect
	github.com/klauspost/cpuid/v2 v2.2.4 // indirect
	github.com/kr/pretty v0.1.0 // indirect
	github.com/leodido/go-urn v1.2.4 // indirect
	github.com/mattn/go-isatty v0.0.19 // indirect
	github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd // indirect
	github.com/modern-go/reflect2 v1.0.2 // indirect
	github.com/pelletier/go-toml/v2 v2.0.8 // indirect
	github.com/twitchyliquid64/golang-asm v0.15.1 // indirect
	github.com/ugorji/go/codec v1.2.11 // indirect
	go.uber.org/multierr v1.11.0 // indirect
	golang.org/x/arch v0.3.0 // indirect
	golang.org/x/crypto v0.9.0 // indirect
	golang.org/x/net v0.10.0 // indirect
	golang.org/x/sys v0.8.0 // indirect
	golang.org/x/text v0.9.0 // indirect
	google.golang.org/protobuf v1.30.0 // indirect
	gopkg.in/check.v1 v1.0.0-20190902080502-41f04d3bba15 // indirect
	gopkg.in/natefinch/lumberjack.v2 v2.2.1 // indirect
	gopkg.in/yaml.v2 v2.4.0 // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
)
