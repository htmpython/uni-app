<template>
	<view class="post-box">
		<view class="post-item" v-for="(item,index) in post_list" :key="index">
			<view class="left">
				<image :src="item.img_url" mode="aspectFill"></image>
			</view>
			<view class="right">
				<view class="user-info">
					<image :src="item.avatar_url" mode="aspectFill"></image>
					<text>{{item.user_name}}</text>
				</view>
				<view class="post-content">
					{{item.content}}
				</view>
			</view>

		</view>
	</view>
</template>

<script>
	export default {
		name: "tong-post-list",
		props: {
			post_list: {
				type: Array,
				default: {}
			}
		}
	}
</script>

<style lang="scss">
	// 动态区域样式
	.post-box {
		.post-item {
			display: flex;
			background-color: #FFFFFF;
			margin: 30rpx;
			padding: 30rpx;
		}

		.left {
			width: 360rpx;
			height: 180rpx;
			margin-right: 30rpx;
			border-radius: 24rpx;
			overflow: hidden;

			image {
				width: 100%;
				height: 100%;
			}
		}

		.right {

			width: 420rpx;

			.user-info {
				display: flex;
				align-items: center;

				image {
					width: 46rpx;
					height: 46rpx;
					border-radius: 50%;
					margin-top: 8rpx;
				}

				text {
					margin-top: 8rpx;
					margin-left: 22rpx;
					font-size: 28rpx;
					word-break: break-all;
					word-wrap: break-word;
					display: -webkit-box;
					-webkit-box-orient: vertical;
					-webkit-line-clamp: 1;
					overflow: hidden;
					text-overflow: ellipsis;
				}

			}

			.post-content {
				color: #303133;
				margin-top: 12rpx;
				font-size: 22rpx;
				word-break: break-all;
				word-wrap: break-word;
				display: -webkit-box;
				-webkit-box-orient: vertical;
				-webkit-line-clamp: 4;
				overflow: hidden;
				text-overflow: ellipsis;
			}
		}



	}

	// 暗黑模式下的样式
	@media (prefers-color-scheme: dark) {
		// 最新动态
		.post-box {
			.post-item {
				background-color: #303133;

				.post-content {
					color: #d6d6d6;
				}
			}
		}
	}
</style>