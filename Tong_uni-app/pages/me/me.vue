<template>
	<view v-if="user_info !== ''">
		<!-- 顶部图片区域 -->
		<image class="top-img" src="../../static/me/bg15.svg" mode="aspectFill"></image>

		<!-- 用户功能区域 -->
		<view class="user-box" >
			<!-- 用户信息 -->
			<view class="info-box">
				<image class="avatar" :src="avatar_url" mode="scaleToFill" @tap="touser_info"></image>
				<view class="user-info" v-if="user_info.length !== 0">
					<view class="nick-name" @tap="touser_info">{{ user_info.name}}</view>
					<view class="description" @tap="touser_info">{{ user_info.introduction }}</view>
				</view>
				<view class="user-info" v-else>
					<view class="nick-name">游客用户</view>
					<view class="description">头像与昵称随机生成🐳</view>
				</view>
				<image class="update" src="../../static/me/update.svg" mode="aspectFill"></image>
			</view>
			<!-- 功能金刚区 -->
			<view class="vajra-box">

				<u-grid :border="false" @click="click" col="3">
					<u-grid-item v-for="(item,index) in vajra_list" :key="index" @click="vajarTo(item.target_url)">
						<image :src="'../../static/me/' + item.icon" mode="aspectFill"></image>
						<text>{{item.text}}</text>
					</u-grid-item>
				</u-grid>
				<u-toast ref="uToast" />
			</view>
		</view>


		<!-- 拓展功能区 -->
		
		<view class="extras-box">
			
			<button class="item" hover-class="item-hover" open-type="contact">
				<view class="item">
					<image class="icon" src="../../static/me/extra-1.svg" mode="aspectFill"></image>
					<view class="text">联系客服</view>
				</view>

				<image class="more" src="../../static/me/more.svg" mode="aspectFill"></image>
			</button>

			<button class="item" hover-class="item-hover" @tap="clearCache()">
				<view class="item">
					<image class="icon" src="../../static/me/extra-2.svg" mode="aspectFill"></image>
					<view class="text">清除缓存</view>
				</view>

				<image class="more" src="../../static/me/more.svg" mode="aspectFill"></image>
			</button>

			<button class="item" hover-class="item-hover" @tap="logout()">
				<view class="item">
					<image class="icon" src="../../static/me/extra-3.svg" mode="aspectFill" ></image>
					<view class="text">退出登录</view>
				</view>

				<image class="more" src="../../static/me/more.svg" mode="aspectFill"></image>
			</button>
			<u-toast ref="uToast" />
		</view>

	</view>
</template>

<script>
	import {
		methods,
		onLoad
	} from '../../uni_modules/uview-ui/libs/mixin/mixin';
	export default {
		data() {
			return {
				vajra_list: [{
					icon: 'vajra-1.svg',
					text: '主页'
				}, {
					icon: 'vajra-2.svg',
					text: '点赞'
				}, {
					icon: 'vajra-3.svg',
					text: '收藏'
				}, ],
				extra_list: [{
					icon: 'extra-1.svg',
					text: '联系客服',
					method: 'contactService'
				}, {
					icon: 'extra-2.svg',
					text: '清除缓存',
					method: 'clearCache'
				}, {
					icon: 'extra-3.svg',
					text: '退出登录',
					method: 'logout'
				}],
				user_info: "",
				avatar_url:"../../static/me/user.png"

			};
		},
		onLoad() {

			this.checkLoginState()
			this.reload()

		},
		methods: {
			// 联系客服
			contactService(){
				
			},
			// 跳转个人信息修改页
			touser_info(){
				uni.navigateTo({
					url:"/pages/me/me_info"
				})
			},
			
			// 清楚缓存
			clearCache(){
				this.$refs.uToast.show({
					message:'清除缓存成功！正在退出登录',
					type:'success',
					complete(){
						//清除缓存
						uni.clearStorageSync(),
						// 跳转首页
						uni.reLaunch({
							url:"/pages/index/index"
						})
					}
				})
			},
			
			// 退出登录
			
			logout() {
				this.$refs.uToast.show({
					message: '退出成功！',
					type: 'success',
					complete() {
						// 清楚缓存
						uni.clearStorageSync(),
						// 跳转首页
						uni.reLaunch({
							url:"/pages/index/index"
						})
					}
				})
			},

			// 检查缓存
			checkLoginState() {
				//  如果已经登录过(有token缓存)
				if (this.$public.loginState()) return
				//  没有登录过(无token)
				uni.navigateTo({
					url: "/pages/me/nologin"
				})
			},
			// 重载数据
			reload() {
				const user_info = this.user_info = uni.getStorageSync("user_info")
				this.avatar_url = user_info.avatar_url
			}
		}
	};
</script>

<style lang="scss">
	// 顶部样式
	.top-img {
		width: 100%;
		height: 360rpx;
		display: block;
	}

	// 用户信息样式
	.user-box {
		background-color: #FFFFFF;
		margin: 0 30rpx;
		border-radius: 20rpx;

		.info-box {
			display: flex;
			padding: 48rpx 48rpx;
			align-items: flex-end;
			position: relative;

			.avatar {
				height: 120rpx;
				width: 120rpx;
				border-radius: 50%;
				margin-right: 36rpx;
			}

			.user-info {
				.nick-name {
					font-size: 48rpx;
				}

				.description {
					color: #807c7c;
					font-size: 24rpx;
					margin-top: 12rpx;
				}
			}

			.update {
				width: 50rpx;
				height: 50rpx;
				position: absolute;
				right: 80rpx;
				bottom: 80rpx;
			}

		}

		.vajra-box {

			image {
				height: 80rpx;
				width: 80rpx;
			}

			text {
				margin: 6rpx 0 10rpx;
				color: #807c7c;
				font-size: 24rpx
			}
		}


	}

	button {
		padding: 0;
		background-color: #FFFFFF;
	}

	button::after {
		border: 0 solid rgba(0, 0, 0, .2);
	}

	.extras-box {
		border-radius: 20rpx;
		padding: 2rpx;
		margin: 25rpx;

		button {
			display: flex;
			align-items: center;
			margin-top: 4rpx;
			justify-content: space-between;

			.item {
				display: flex;
				align-items: center;
			}

			.icon {
				width: 65rpx;
				height: 65rpx;
				padding: 16rpx 32rpx 6rpx 32rpx;
			}

			.more {
				width: 55rpx;
				height: 55rpx;
			}

			.text {
				font-size: 30rpx;
			}
		}


	}

	.item-hover {
		background-color: #f0f3f3;
	}

	@media (prefers-color-scheme: dark) {
		.user-box {
			background-color: #1e1e1e;
		}

		.extras-box {
			background-color: #1e1e1e;

			button {
				background-color: #1e1e1e;
			}

			.item-hover {
				background-color: #191919;
			}

		}

	}
</style>