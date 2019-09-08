# python-aws-api-test
Python test

# テスト対象

```
/users/
	* GET　ユーザー一覧取得
		* 権限によってデータは変わる
	* POST　承認後の正式ユーザー登録

/users/{id}/
	* GET　ユーザー情報詳細取得
		* 権限によっては取得できない
	* PUT　ユーザー情報更新
	* DELETE  ユーザー削除

-------------------------------------------------

/users/{id}/roles
	* POST　ユーザーにRoleを追加

/users/{id}/roles/{Role名}
	* DELETE ユーザーからRoleをはく奪

-------------------------------------------------

/request_users/ 
	* GET　申請前のユーザー一覧取得
	* POST　ユーザー申請

/request_users/{id}
	* GET　申請前のユーザー詳細取得
	* PUT　申請前のユーザー詳細更新
	* DELETE  申請前のユーザー削除

-------------------------------------------------

/request_managers/  [No Auth]
        * POST  Managerの申請
	    * 認証不要な特殊なAPI 
/login_user/ 
	* GET　ログインユーザー情報取得
	    * ID指定不要のAPI 
```
