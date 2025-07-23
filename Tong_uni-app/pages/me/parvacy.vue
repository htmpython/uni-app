<template>
	<view>
		<!-- 协议时间 -->
		<view class="que-time">
			<view class="que-time-float">
				更新日期：2025年5月25日
			</view>
			<view class="que-time-float">
				生效日期：2025年5月25日
			</view>

		</view>

		<view class="describe">
			为切实保护小程序用户个人信息，优化用户体验，通通UGC小程序
			(以下或称“开发者”）根据现行法规及政策，制定《个人信息
			保护政策》（以下简称“本政策”）。本政策将详细说明我们
			在获取、使用、管理及保护用户个人信息方面的政策及措
			施。

		</view>
		<view class="title">
			1.开发者处理的信息
		</view>
		<view class="describe">
			1.1 为了初始化账户的头像昵称，开发者将在获取你的明示同意后，收集你的微信昵称、头像。
		</view>
		<view class="describe">
			1.2 为了在发帖时附加位置信息，开发者将在获取你的明示同意后，收集你的位置信息。
		</view>
		<view class="describe">
			1.3 为了应网信办《互联网论坛社区服务管理规定》要求，开发者将在获取你的明示同意后，收集你的手机号。
		</view>
		<view class="describe">
			1.4 为了实现海报分享功能，开发者将在获取你的明示同意后，使用你的相册（仅写入）权限。
		</view>
		<view class="describe">
			1.4 开发者收集你选中的照片或视频信息，用于在发帖、发评论时附加图片、视频。
		</view>
		
		<view class="title">
			2.你的权益
		</view>
		<view class="describe">
			关于你的个人信息，你可以通过以下方式与开发者联系，行使查阅、复制、更正、删除等法定权利
		</view>
		<view class="describe">
			邮箱: 2227638014@qq.com
		</view>
		<view class="title">
			3.开发者对信息的存储
		</view>
		<view class="describe">
			开发者承诺，除法律法规另有规定外，开发者对你的信息的保存期限应当为实现处理目的所必要的最短时间。
		</view>
		<view class="title">
			4.信息的使用规则
		</view>
		<view class="describe">
			开发者将会在本指引所明示的用途内使用收集的信息
			如开发者使用你的信息超出本指引目的或合理范围，开发者必须在变更使用目的或范围前，再次以站内信、公告方式告知并征得你的明示同意。
		</view>
		<view class="title">
			5.信息对外提供
		</view>
		<view class="describe">
			开发者承诺，不会主动共享或转让你的信息至任何第三方，如存在确需共享或转让时，开发者应当直接征得或确认第三方征得你的单独同意。
			开发者承诺，不会对外公开披露你的信息，如必须公开披露时，开发者应当向你告知公开披露的目的、披露信息的类型及可能涉及的信息，并征得你的单独同意。
		</view>
		<view class="title">
			6.客服联系方式
		</view>
		<view class="describe">
			若你认为开发者未遵守上述约定，或有其他的投诉建议、或未成年人个人信息保护相关问题，可通过以下方式与开发者联系；或者向微信进行投诉。
		</view>
		<view class="describe">
			邮箱: 2227638014@qq.com
		</view>
		<view class="describe">
			联系时请备注相关信息
		</view>
		
	</view>
</template>

<script>
	export default {
		data() {
			return {

			}
		},
		methods: {

		}
	}
</script>

<style>



	/* 协议时间 */
	.que-time {
		overflow: hidden;
		margin: 38upx;
	}

	.que-time-float {
		float: right;
	}

	.describe {
		font-size: 30upx;
		margin: 38rpx;
		line-height: 50rpx;
	}

	.title {
		font-size: 40rpx;
		margin: 38rpx;
	}

	page {
		background-color: #f7f7f7;
		overflow-x: hidden;
	}

	/* 暗黑模式下应用的样式 */
	@media (prefers-color-scheme: dark) {
		page {
			background: #111111;
		}
	}
</style>
