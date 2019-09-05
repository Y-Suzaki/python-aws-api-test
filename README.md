# python-aws-api-test
Python test

# テスト対象

```
/login_user/ 
	* GET　ログインユーザー情報取得
/users/
	* GET　ユーザー一覧取得
		* 権限によってデータは変わる
	* POST　承認後の正式ユーザー登録
/users/{id}/
	* GET　ユーザー情報詳細取得
		* 権限によっては取得できない
	* PUT　ユーザー情報更新
/users/{id}/roles
	* POST　ユーザーにRoleを追加
/users/{id}/roles/{Role名}
	* DELETE ユーザーからRoleをはく奪
/request_users/ 
	* GET　申請前のユーザー一覧取得
	* POST　申請
/request_users/{id}
	* GET　申請前のユーザー詳細取得
	* PUT　申請前のユーザー詳細更新
```