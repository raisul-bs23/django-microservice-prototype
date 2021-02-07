package routes

import (
	"github.com/gin-gonic/gin"
	"permission/api"
)

// Hello ...
func Hello(r *gin.Engine) {
	r.GET("/permission/get-all-permission", api.Hello)
}
